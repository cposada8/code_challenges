def balanced_parens(n):
    # Your code here!
    parens = set([""])
    new_parens = []
    for i in range(n):
        new_parens = []
        for elem in parens:
            new1 = "()"+elem
            new2 = elem+"()"
            new3 = "("+elem+")"
            new_parens.append(new1)
            new_parens.append(new2)
            new_parens.append(new3)
            news = []
            for j in range(len(elem)):
                new_j = elem[:j] + "()" + elem[j:]
                new_parens.append(new_j)
        parens = set(new_parens)
    return list(parens)


if __name__ == "__main__":
    print(balanced_parens(3))
