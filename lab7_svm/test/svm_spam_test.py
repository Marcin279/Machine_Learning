import svm_spam


def test_read_file():
    file_path = "./data/emailSample2.txt"
    print(svm_spam.read_file(file_path))
