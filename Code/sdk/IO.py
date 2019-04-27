class IO:
    def __init__(self):
        pass
    
    def ReadFile(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as f:
            return f.readlines()

    def ReadFiles(self, file_path, perfix, min_idx, max_idx):
        file_list = []
        for i in range(min_idx, max_idx+1):
            file_list.append(self.ReadFile(('%s/%s-%d')%(file_path, perfix, i)))
        return file_list

    def WriteFile(self, data, file_path):
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(data)
        
    def WriteFiles(self, data_list, file_path, perfix, min_idx, max_idx):
        for i, j in zip(range(min_idx, max_idx+1), data_list):
            self.WriteFile(j, "%s/%s-%d"%(file_path, perfix, i))

    def SaveArray(self, arrays, save_path):
        np.save(save_path, arrays)

    def ReadArray(self, save_path):
        return np.load(save_path)

if __name__ == "__main__":
    pass
