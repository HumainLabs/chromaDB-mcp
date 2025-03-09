#!/usr/bin/env python3
"""
Data Migration Script for ChromaDB MCP Server

This script helps migrate data from the old src/chroma/data directory
to the new src/chroma_mcp/data directory.
"""

import os
import shutil
import sys

def migrate_data():
    """Migrate data from old to new location."""
    old_dir = os.path.join("src", "chroma", "data")
    new_dir = os.path.join("src", "chroma_mcp", "data")

    # Check if old directory exists
    if not os.path.exists(old_dir):
        print(f"No data directory found at {old_dir}")
        print("No migration needed.")
        return False
    
    # Create new directory if it doesn't exist
    os.makedirs(new_dir, exist_ok=True)
    
    # Copy all files
    items = os.listdir(old_dir)
    if not items:
        print(f"No data found in {old_dir}")
        return False
    
    print(f"Found {len(items)} items to migrate")
    
    # Copy each item from old to new directory
    for item in items:
        old_path = os.path.join(old_dir, item)
        new_path = os.path.join(new_dir, item)
        
        if os.path.isdir(old_path):
            # Copy directory recursively
            shutil.copytree(old_path, new_path, dirs_exist_ok=True)
            print(f"Copied directory: {item}")
        else:
            # Copy file
            shutil.copy2(old_path, new_path)
            print(f"Copied file: {item}")
    
    print("\nMigration completed successfully!")
    print(f"Data migrated from {old_dir} to {new_dir}")
    print("\nYou can now remove the old directory if you wish with:")
    print(f"rm -rf {old_dir}")
    
    return True

if __name__ == "__main__":
    print("ChromaDB MCP Server - Data Migration Utility\n")
    
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)
    
    try:
        migrate_data()
    except Exception as e:
        print(f"Error during migration: {e}")
        sys.exit(1) 