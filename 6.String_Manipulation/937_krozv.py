# Reorder Log Files
class ReorderLogFiles:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        log_list = []
        for log in logs:
            identifier, *info = log.split(' ')
            log = [identifier, info]
            log_list.append(log)
        let_list = []
        dig_list = []

        for log in log_list:
            # log가 문자인지, 숫자인지 구별
            if log[1][0].isalpha():
                let_list.append(log)
            else:
                dig_list.append(log)
        # 문자로 만 이루어진 log를 정렬
        let_list.sort(key=lambda x: (x[1], x[0]))

        let_list.extend(dig_list)
        output_list = []
        for log in let_list:
            output = log[0] + ' ' + ' '.join(log[1])
            output_list.append(output)
        return output_list



c = ReorderLogFiles()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
c.reorderLogFiles(logs)
