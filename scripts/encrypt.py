import numpy as np
letters='ABCDEFGHIGKLMNOPQRSTUVWXYZ'
a=np.array([[3,5],[1,2]])#矩阵A,这个需要需要是可逆的
b=np.array([2,3])#向量b
def encrypt(plaintext):
    """加密算法，线性方程式，方程和矩阵"""
    cipher=""
    for i in range(0, len(plaintext), 2):
        first_letter=plaintext[i]
        second_letter= plaintext[i+1]
        p_1=letters.find(first_letter)
        p_2=letters.find(second_letter)
        p=np.array([p_1,p_2])
        cipher_vector=np.dot(a,p)+b#np.dot函数将数组A和数组p进行矩阵乘法运算
        c_1=cipher_vector[0]%26
        c_2=cipher_vector[1]%26
        cipher +=letters[c_1]
        cipher +=letters[c_2]
    return cipher
def decrypt(cipher):
    """解密算法"""
    #a_inverse=np.array([[2,-5],[-1,3]])#矩阵A的逆矩阵A_inv，可以使用numpy库中的np.linalg.inv函数来计算逆矩阵

    a_inverse = np.linalg.inv(a)#计算逆矩阵
    a_inv_rounded = np.round(a_inverse).astype(int)#逆矩阵的元素转换为整数
    plaintext=""
    for i in range(0, len(cipher),2):
        first_letter=cipher[i]
        second_letter=cipher[i + 1]
        c_1=letters.find(first_letter)
        c_2=letters.find(second_letter)
        c=np.array([c_1,c_2])
        plaintext_vector=np.dot(a_inv_rounded,c)-np.dot(a_inv_rounded, b)
        p_1=plaintext_vector[0]%26
        p_2=plaintext_vector[1]%26
        plaintext +=letters[p_1]
        plaintext +=letters[p_2]
    return plaintext

print(encrypt('HELPSAVEMEOP'))#输入的字符程度必须是双数
print(decrypt('RSGSEVHGGXPV'))
