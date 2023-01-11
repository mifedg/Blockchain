import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'  # переходим в директорию


def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read() #получаем название файла

    return hashlib.md5(file).hexdigest() #создаем хэш
def get_files():
    files = os.listdir(blockchain_dir) # получили список всех файлов в этой папке
    return sorted([int(i) for i in files]) #отсортровали этот список, каждый элемент списка приводим к типу инт

def check_integrity(): #проверка целостности
    #1/ Считать хэш предыдущего блока
    files = get_files() #[1, 2, 3, 4, 5]

    results = []
    for file in files[1:]: #[2, 3, 4, 5]
        f = open(blockchain_dir + str(file)) # '2'
        h = json.load(f)['hash'] #значение ключа hash

        #2/ вычисляем хэш предыдущего блока
        prev_file = str(file - 1) #какой предыдущий блок
        actual_hash = get_hash(prev_file)#вычисляем хэш предыдущего

        #3 сравнить значение в блоке и полученное
        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

       # print('block {} is: {}'.format(prev_file, res))
        results.append({'block': prev_file, 'result': res})
    return results


def write_block(name, amount, to_whom, prev_hash=''):
    files = get_files()
    prev_file = files[-1] #индекс последнего блока в папке

    filename = str(prev_file + 1)#индекс нового блока

    prev_hash = get_hash(str(prev_file))# преопределяем хэш предыдущего блока

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}
    with open(blockchain_dir +filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    #write_block(name='oleg', amount=5, to_whom='ksu')
    print(check_integrity())

if __name__ == '__main__':
    main()
