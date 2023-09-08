
__MAIL_USER__ = "nzhang@caltech.edu"


def generate_slurm_input(
        filename: str,
        job_name: str,
        outputname: str,
        time: str = "7-00:00:00",
        errorname: str = "error.log",
        nodes: int = 1,
        partition: str = "serial,parallel",
        # node_range: list = [0, 10],
        memory: int = 100,
        commond: str = "python3 main.py",
):
    with open(filename, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("#SBATCH --time=%s\n" % (time))
        f.write("#SBATCH -J %s\n" % (job_name))
        f.write("#SBATCH -o %s\n" % (outputname))
        f.write("#SBATCH -e %s\n" % (errorname))
        f.write("#SBATCH --mail-user=%s\n" % __MAIL_USER__)
        f.write("#SBATCH --mail-type=all\n")
        f.write("#SBATCH --partition=%s\n" % (partition))
        f.write("#SBATCH --nodes=%d\n" % (nodes))
        f.write("#SBATCH --exclusive\n")
        f.write("#SBATCH -x pauling[001-049]\n")
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
