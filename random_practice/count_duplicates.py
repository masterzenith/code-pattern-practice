def countDupes(root, prev):
    duplicates = 0
    if root is None:
        return duplicates
    duplicates += countDupes(root.left, prev)
    if root != prev and root.value == prev.value:
        duplicates += 1
    duplicates += countDupes(root.right, root)
    return duplicates


def main():
    print(countDupes(2, 1))


if __name__ == "__main__":
    main()
