
__MAIL_USER__ = "nzhang@caltech.edu"


def generate_slurm_input(
        filename: str,
        job_name: str,
        outputname: str,
        errorname: str = "error.log",
        nodes: int = 1,
        node_range: list = [0, 10],
        memory: int = 100,
        commond: str = "python3 main.py",
):
    with open(filename, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("#SBATCH -J %s\n" % (job_name))
        f.write("#SBATCH -o %s\n" % (outputname))
        f.write("#SBATCH -e %s\n" % (errorname))
        f.write("#SBATCH --mail-user=%s\n" % __MAIL_USER__)
        f.write("#SBATCH --mail-type=all\n")
        f.write("#SBATCH --partition=serial,parallel\n")
        f.write("#SBATCH --nodes=%d\n" % (nodes))
        f.write("#SBATCH --exclusive\n")
        f.write("#SBATCH -x pauling[%d-%d]\n" % (node_range[0], node_range[1]))
        f.write("#SBATCH --mem=%dG\n" % (memory))
        f.write("export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE\n")
        f.write("%s\n" % (commond))

    # pass


if __name__ == '__main__':

    generate_slurm_input(
        "test.sh",
        "test",
        "test.out")

    pass
