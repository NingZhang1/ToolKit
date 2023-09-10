
__MAIL_USER__ = "nzhang@caltech.edu"


def generate_slurm_input(
        filename: str,
        job_name: str,
        outputname: str,
        exclusive = True,
        time: str = "7-00:00:00",
        errorname: str = "error.log",
        nodes: int = 1,
        partition: str = "serial,parallel",
        # node_range: list = [0, 10],
        # not_equipment = "pauling[001-040]",
        not_equipment = None,
        memory: int = 100,
        additional_option = None,
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
        if exclusive:
            f.write("#SBATCH --exclusive\n")
        if not_equipment is not None:
            f.write("#SBATCH -x %s\n" % (not_equipment))
        f.write("#SBATCH --mem=%dG\n" % (memory))
        f.write("export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE\n")
        if additional_option is not None:
            for tmp in additional_option:
                f.write("%s" % (tmp))
        f.write("%s\n" % (commond))

    # pass


if __name__ == '__main__':

    generate_slurm_input(
        "test.sh",
        "test",
        "test.out")

    pass
