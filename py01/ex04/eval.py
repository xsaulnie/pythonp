class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if (type(coefs) is not list or type(words) is not list):
            return -1
        for x in coefs:
            if (type(x) is not float):
                return -1
        for y in words:
            if (type(y) is not str):
                return -1
        if (len(coefs) != len(words)):
            return -1
        res = 0
        for x, y in zip(coefs, words):
            res = res + len(y) * x
        return res
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if (type(coefs) is not list or type(words) is not list):
            return -1
        for x in coefs:
            if (type(x) is not float):
                return -1
        for y in words:
            if (type(y) is not str):
                return -1
        if (len(coefs) != len(words)):
            return -1
        res = 0

        for idx, coef in enumerate(coefs):
            res = res + len(words[idx]) * coef
        return res


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))