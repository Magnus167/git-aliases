import os
import glob
import mdformat, mdformat_gfm

from typing import Dict, List


SCRIPTS_DIR = "aliases"


def get_files(path: str):
    # recursively
    return glob.glob(f"{path}/**/*", recursive=True)


def load_file(file: str) -> Dict[str, str]:
    with open(file, "r") as f:
        content = f.read()

    iscomment = lambda x: str(x).startswith("# ")

    # get all the commented lines
    lines = content.split("\n")

    comments_idx = [i for i, line in enumerate(lines) if iscomment(line)]
    comment = "\n".join([lines[i][2:] for i in comments_idx if lines[i].strip() != ""])
    comment = mdformat.text(comment)
    script_idx = [
        i
        for i, line in enumerate(lines)
        if (not iscomment(line)) and (line.strip() != "")
    ]
    script = "\n".join([lines[i] for i in script_idx])
    if not comment or not script:
        return {}

    titlex = comment.split("\n")[0][2:]
    idx_entry = f'[{titlex.split("-")[0].strip()}](#{titlex.strip().replace(" ", "-")})'

    return {
        "path": os.path.basename(file),
        "markdown": comment,
        "script": script,
        "idx": idx_entry,
    }


def load_readme(file: str = "README.md") -> str:
    with open(file, "r") as f:
        content = f.read()
    return content


def compile_scripts(files: List[Dict[str, str]]):
    files = [fx for fx in files if bool(fx)]

    add_header_level = lambda mdx: "\n".join(
        [(f"#{lx}" if lx.startswith("#") else lx) for lx in str(mdx).split("\n")]
    )

    mds = [
        f"\n\n"
        + add_header_level(fx["markdown"])
        + "\n\n### Script:\n\n"
        + f"```bash\n{fx['script']}\n```\n"
        + "\n\n---\n\n"
        for ix, fx in enumerate(files)
    ]
    mds = "\n".join(mds)

    # lef link to header with pathname as anchor
    idxmd = "\n".join([" - " + str(fx["idx"]) for fx in files])
    mds = f"## Index\n\n{idxmd}\n\n{mds}"

    # mds = mdformat.text(mds)
    return mds


def generate_index(compiled_scripts: str, readme: str, file: str = "index.md"):
    readme += "\n\n" + compiled_scripts
    readme = mdformat.text(readme, extensions={"gfm"})
    with open(file, "w") as f:
        f.write(readme)


def main():
    compiled_scripts = compile_scripts([load_file(fx) for fx in get_files(SCRIPTS_DIR)])
    readme = load_readme()
    generate_index(compiled_scripts, readme)


if __name__ == "__main__":
    main()
