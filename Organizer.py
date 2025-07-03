import os
import shutil
import argparse
from pathlib import Path
from rich.console import Console

console = Console()

# File type categories
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Archives': ['.zip', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov'],
    'Others': []
}

def organize_folder(folder_path, dry_run=False):
    if not os.path.isdir(folder_path):
        console.print(f"[bold red]Error:[/] Folder '{folder_path}' does not exist.")
        return

    files_moved = 0
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if os.path.isfile(full_path) and not item.startswith('.'):
            ext = Path(item).suffix.lower()
            category = next((cat for cat, exts in FILE_TYPES.items() if ext in exts), 'Others')
            dest_folder = os.path.join(folder_path, category)

            if dry_run:
                console.print(f"[yellow]Would move:[/] {item} → {category}/")
            else:
                os.makedirs(dest_folder, exist_ok=True)
                try:
                    shutil.move(full_path, os.path.join(dest_folder, item))
                    console.print(f"[green]Moved:[/] {item} → {category}/")
                    files_moved += 1
                except Exception as e:
                    console.print(f"[red]Failed to move {item}:[/] {e}")

    if not dry_run:
        console.print(f"\n[bold cyan]✅ Done:[/] Organized {files_moved} file(s).")

def parse_args():
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("path", help="Path to folder to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    expanded_path = os.path.expanduser(args.path)
    organize_folder(expanded_path, dry_run=args.dry_run)

