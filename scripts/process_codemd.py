import os
import sys
import zlib
import requests
import base64

PLANTUML_SERVER = "http://www.plantuml.com/plantuml"

# Custom Base64 encoding for PlantUML
def plantuml_encode(text):
    # UTF-8 encoding
    utf8_encoded = text.encode('utf-8')

    # Deflate compression
    compressed = zlib.compress(utf8_encoded, 9)[2:-4]

    # Base64-like encoding with custom character mapping
    base64_encoded = base64.b64encode(compressed).decode('utf-8')

    # Replace Base64 characters with PlantUML's custom Base64 characters
    plantuml_encoded = base64_encoded.translate(
        str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
                      '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'))

    return plantuml_encoded


def process_codemd(source_file, output_dir):
    destination_file = os.path.basename(source_file).replace('.src.md', '.md')
    print(f"Processing {source_file}, output_dir {output_dir} saving to {destination_file},")
    # Initialize counter for diagram numbering
    counter = 1
    os.makedirs(output_dir, exist_ok=True)

    # Read the content of the source .codemd file
    with open(source_file, "r") as file:
        lines = file.readlines()

    temp_lines = []
    inside_code_block = False
    code_block = ""

    # Keywords for special diagrams where @startuml/@enduml should not be added
    diagrams_types = ["@staruml", "@startjson", "@startyaml", "@startebnf", "@startregex",
                      "@startsalt", "@startditaa", "@startgantt", "@startchronology", "@startmindmap",
                       "@startwbs", "@startchen"]

    for line in lines:
        if inside_code_block:
            if line.strip() == "```":

                # Wrap the code block with @startuml and @enduml if not already present
                # also cases of special diagrams is covered here.
                if all(s not in code_block for s in diagrams_types):
                    code_block = f"@startuml\n{code_block.strip()}\n@enduml\n"

                is_ditaa = "@startditaa" in code_block

                # End of PlantUML block
                filename = f"{os.path.basename(source_file).replace('.src.md', '')}_diagram_{counter}"
                extension = "svg" if not is_ditaa else "png"
                output_file_path = os.path.join(output_dir, f"{filename}.{extension}")
                print(f'output_file_path: {output_file_path}')

                # Encode the PlantUML code
                encoded_diagram = plantuml_encode(code_block)

                # Send the encoded diagram to the PlantUML server to get the SVG
                response = requests.get(f"{PLANTUML_SERVER}/svg/{encoded_diagram}")

                if response.status_code == 200:
                    # Save the SVG content
                    with open(output_file_path, "wb") as svg_file:
                        svg_file.write(response.content)
                elif response.status_code == 400:
                    print(f"Error in diagram  {filename}")
                    with open(output_file_path, "wb") as svg_file:
                        svg_file.write(response.content)
                else:
                    print(f"Error: Unable to generate diagram for {filename}")
                    print(f"Error status: {response.status_code}")
                    print(f"Error text: {response.reason}")

                # Replace the code block in the Markdown with a link to the SVG
                temp_lines.append(f"![Diagram {counter}](./{output_dir}/{filename})")
                temp_lines.append(f'\n<details>\n <summary>View Source</summary>\n\n')
                temp_lines.append(f'```plantuml\n')
                # Comment out the original PlantUML code block
                temp_lines.append(f"{code_block}")
                temp_lines.append(f'```\n</details>\n')

                counter += 1
                inside_code_block = False
            else:
                code_block += line
            continue
        if line.strip() == "```plantuml":
            inside_code_block = True
            code_block = ''
        else:
            temp_lines.append(line)

    # Write the modified content to the destination .md file
    with open(destination_file, "w") as md_file:
        md_file.writelines(temp_lines)

    print(f"Finished processing {source_file}, saved to {destination_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_codemd.py <source_file.src.md> <destination_folder>")
        sys.exit(1)

    process_codemd(sys.argv[1], sys.argv[2])