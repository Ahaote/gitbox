import json
from datetime import datetime

class StudentManager:

    def __init__(self, file_path='students.json'):
        self.file_path = file_path
        self.students = self._load_data()
        self.current_user = {'name': 'guest', 'is_admin': False}

    # 文件操作；加载数据
    def _load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # 文件操作：保持数据
    def _save_data(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.students, f, indent=2)

    def add_student(self, name, scores):
        new_id = max([s['id'] for s in self.students], default=0) + 1
        self.students.append({
            'id': new_id,
            'name': name,
            'scores': scores,
            'create_time': datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        })
        self._save_data()

    def get_student(self, student_id):
        try:
            return next(s for s in self.students if s['id'] == student_id)
        except StopIteration:
            raise ValueError("学生不存在")
    
    def del_student(self, student_id):
        self.students = [s for s in self.students if s['id'] != student_id]
        self._save_data()

    def show_statistics(self):
        math_scores = [s['scores']['math'] for s in self.students]
        avg = lambda lst : sum(lst)/len(lst) if lst else 0
        print(f"数学平均分：{avg(math_scores):.1f}")


if __name__ == "__main__":
    manager = StudentManager()
    manager.current_user = {'name' : 'admin', 'is_admin': True}

    # 生成学生(自动生成ID)
    manager.add_student("张三", {"math":85, "english":92})
    manager.add_student("李四", {"math":78, "english":88})

    print(manager.get_student(1))

    manager.show_statistics()

    manager.del_student(2)