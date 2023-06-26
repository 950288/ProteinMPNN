import argparse


def main(args):

    pos_list = []
    ranges = args.design_only_positions.split()
    for r in ranges:
        if "-" in r:
            start, end = r.split("-")
            pos_list.extend(list(range(int(start), int(end)+1)))
        else:
            pos_list.append(int(r))

    with open(args.output_path, "w") as f:
        f.write(" ".join(map(str, pos_list)))

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument("--input_path", type=str, help="Path to the parsed PDBs")
    argparser.add_argument("--output_path", type=str, help="Path to the output dictionary")

    args = argparser.parse_args()
    main(args)