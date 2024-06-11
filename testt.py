from cemirutils import CemirUtils

cemir_utils = CemirUtils()


utils = CemirUtils()

# Dosya ve dizinleri listeleme örneği
print(utils.linux_ls("."))


# Dosya oluşturma örneği
print(utils.linux_touch("new_file.txt"))

# Dosyayı gzip ile sıkıştırma örneği
print(utils.linux_gzip("new_file.txt"))

# Dosya içeriğini görüntüleme örneği
print(utils.linux_cat("new_file.txt"))

# Dosya kopyalama örneği
print(utils.linux_cp("new_file.txt", "destination.txt"))

# Dosya taşıma örneği
print(utils.linux_mv("new_file.txt", "/tmp/"))

# Dosya silme örneği
# print(utils.linux_rm("new_file.txt"))

# Yeni bir dizin oluşturma örneği
print(utils.linux_mkdir("new_directory"))

# Boş bir dizini silme örneği
print(utils.linux_rmdir("new_directory"))

# Dosyadan alanları ayırma örneği
print(utils.linux_cut("\t", "1,3", "data.txt"))


# Dizin içinde dosya arama örneği
print(utils.linux_find("/", "new_file.txt"))

# Dosyada desen arama örneği
print(utils.linux_grep("a", "new_file.txt"))