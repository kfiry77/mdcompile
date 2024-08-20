# PlantUML Processing Action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/kfiry77/mdcopile)
![GitHub](https://img.shields.io/github/license/kfiry77/mdcompile)

This GitHub Action processes `.codemd` files, converts them to `.md` files, and embeds PlantUML diagrams using an external PlantUML server. It is designed to be an out-of-the-box solution, requiring minimal configuration.

## Features

- Converts `.codemd` files to `.md` files.
- Automatically detects and processes PlantUML code blocks.
- Embeds diagrams as SVG images directly in the Markdown files.
- Uses an external PlantUML server for fast processing.
- Easy integration with a single line of code.

## Usage

To use this action in your repository, add the following to your GitHub Actions workflow YAML file:

```yaml
jobs:
  plantuml:
    runs-on: ubuntu-latest
    steps:
      - uses: your-username/your-action-repo@v1.0.0
        with:
          output_dir: "plantuml_files"
```

### Inputs

| Input        | Description                                                     | Required | Default         |
|--------------|-----------------------------------------------------------------|----------|-----------------|
| `output_dir` | The directory where the processed `.md` files will be saved.    | Yes      | `plantuml_files` |

### Example Workflow

Here is a full example of a workflow using this action:

```yaml
name: Process PlantUML

on: [push, pull_request]

jobs:
  plantuml:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Process PlantUML files
        uses: your-username/your-action-repo@v1.0.0
        with:
          output_dir: "docs/diagrams"

      - name: Commit and push changes
        run: |
          git config --local user.email "actions@github.com"
          git config --local user.name "GitHub Actions"
          git add .
          if git diff --quiet; then
            echo "No changes to commit."
          else
            git commit -m "Add updated diagrams"
            git push
          fi
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### How It Works

1. **Input Directory**: The Action scans your repository for `.codemd` files.
2. **Processing**: For each `.codemd` file, it converts PlantUML code blocks into SVG diagrams using an external PlantUML server.
3. **Output**: The processed Markdown files are saved in the specified output directory, with diagrams embedded as SVG images.

## Customization

This action uses a constant for the PlantUML server address within the Python script. If you need to customize this, you can modify the Python script in the `scripts` directory.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
