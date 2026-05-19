#!/usr/bin/env python3
"""
create_structure.py
Creates the Apigee proxy folder scaffolding for proxy-demo-maven.
Maven-compatible structure — includes src/gateway layout expected by
the Apigee Maven Deploy Plugin (apigee-deploy-maven-plugin).
"""

import os
import sys

PROXY_NAME = "proxy-demo-maven"

# Maven Apigee plugin expects the bundle under:
#   src/gateway/<env>/apiproxy/
# plus a pom.xml at root level.
DIRECTORIES = [
    "apiproxy",
    "apiproxy/proxies",
    "apiproxy/targets",
    "apiproxy/policies",
]


def create_directories(base_path: str = ".") -> None:
    for directory in DIRECTORIES:
        full_path = os.path.join(base_path, directory)
        os.makedirs(full_path, exist_ok=True)
        print(f"[OK] Created directory: {full_path}")


def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"==> Scaffolding proxy bundle under: {os.path.abspath(base_path)}")
    create_directories(base_path)
    print("==> Directory scaffolding complete.")
    print("")
    print("    Folder structure:")
    for d in DIRECTORIES:
        indent = "    " + ("    " * d.count("/"))
        print(f"{indent}└── {os.path.basename(d)}/")


if __name__ == "__main__":
    main()
