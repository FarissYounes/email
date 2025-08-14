import os
import subprocess
import codecs
import argparse
import csv

def run_git_command(args, cwd=None):
    """Exécute une commande Git (Python 2.7)."""
    cmd = ["git"] + args
    try:
        output = subprocess.check_output(cmd, cwd=cwd)
        print(output)
        return output
    except subprocess.CalledProcessError as e:
        print("Erreur git {}:\n{}".format(" ".join(args), e.output))
        return None

def update_ft(tmp_path):
    repo_path = os.path.abspath(os.path.join(tmp_path, "../../../"))

    csv_lect = []
    with codecs.open('output.csv', 'r', encoding='utf-8') as f:
        csv_lect = list(csv.reader(f))

    temp_path = tmp_path
    for file in os.listdir(temp_path):
        chemin_complet = os.path.join(temp_path, file)
        if os.path.isfile(chemin_complet):
            for line in csv_lect:
                if file == line[2][1:]:
                    branch_name = "update_ref_files"

                    # Vérifie si la branche existe
                    branches = run_git_command(["branch", "--list", branch_name], cwd=repo_path) or ""
                    if branch_name not in branches:
                        run_git_command(["checkout", "master"], cwd=repo_path)
                        run_git_command(["checkout", "-b", branch_name], cwd=repo_path)

                    run_git_command(["checkout", "-f", branch_name], cwd=repo_path)

                    with codecs.open(chemin_complet, 'r', encoding='utf-8') as f_in:
                        lines = f_in.readlines()
                    with codecs.open(os.path.join(repo_path, "../data", line[1]), 'w', encoding='utf-8') as f_out:
                        f_out.writelines(lines)

                    run_git_command(["add", "functional-tests/data/"], cwd=repo_path)

                    commit_message = "[{}] - Update reference file : {}".format(line[3][15:], line[1])
                    run_git_command(["commit", "-m", commit_message], cwd=repo_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("agent", type=str, help="agent_name")
    args = parser.parse_args()

    update_ft("D:/power-{}/controller/functest/tmp".format(args.agent))
