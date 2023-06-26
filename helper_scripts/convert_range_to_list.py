import argparse

def main(args):
    pos_list = []
    ranges = args.range.split()
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

    args = argparser.parse_args()
    main(args)