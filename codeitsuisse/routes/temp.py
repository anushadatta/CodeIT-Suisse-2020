a = ["-vc+vdtysbcjcbjmqzdwsiycvcmzguspyxubqh-qhsrh-cublxduggz", "vcdtysbcjcbjzq+uzdws-iycvcmzguspyxubmj-qhsrhcublxduggz",
"vcdtysbcjcbjzqz-dwszycvcmzguspyxubq+ghqhsrhcud-lxduggz", "vcdtysbcjc+lbjzqzdwsiy+acvcmzgus-pyxubq-hqhsrhcu-blxduggz",
"vcdtysb+mcjcbjzqzdws+aiyckcmzguspyxubqhohs-rhcublxduggz", "vcdtys+cb+xcjcbjzqzdwsi-ycvcmzguspyxubq+ghqhsrhcublxdu-ggz",
"v-cdtysbcjcbj-zqzdw+ysiycvcmzguspyx-ubqhqhsrhcub-lxduggz", "-vcdtysbc+gjvbjzqzdwszccvcmzguspyxubqh-qhsrhcublxduggz",
"hvcdtysbcjcbjzqz+tdwsiycvcmzguspyxubq+uhqhsrh+bcublxduf-gz", "qcdtysbcjc-bjz-qzdwsiycvcmzhuspyxujkhqhsrhcublxduggz"]

for i in a:
    j =0
    res = ""
    while(j < len(i)):
        # print(j,i[j],end="   ")
        if i[j]=="-":
            j+=1
        elif i[j]!="+":
            res = res + i[j]
        j+=1

    print(res)