def main():
    print("Hello from word-translation!")


if __name__ == "__main__":
    from dict_cc import contents, g_to_e
    with open("extract1.txt") as ex:
        ex = ex.read()
    print(ex)
    print("\n")
    # for word in ex.split():
    #     print(word, "|", g_to_e(word))
    print(" ".join([g_to_e(word) for word in ex.split()]))
        
