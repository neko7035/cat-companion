# 🐱 CatCompanion
A terminal-based virtual cat companion system.  
一个基于终端的虚拟猫陪伴系统。
---
## 📌 Version | 当前版本
**v0.2**
---
## 🎯 Project Description | 项目介绍
**EN:**  
CatCompanion is a command-line virtual pet written in Python.  
It maintains persistent state, supports time-based behavior updates, and allows interactive commands.

**中文：**  
CatCompanion 是一个使用 Python 编写的终端虚拟宠物系统。  
它支持状态持久化、基于时间变化的行为更新，以及交互式命令输入。

The long-term goal is to evolve it into a more emotionally responsive companion system.  
长期目标是将其发展为一个具有情绪反馈能力的陪伴型系统。

---

## 🧠 Current Features (v0.2) | 当前功能

### 1️⃣ Core Attributes | 核心属性

- mood (0-100) —— 心情值
- trust (0-100) —— 信任值
- sleep_score (0-100) —— 睡眠值

All values are automatically clamped within valid ranges.  
所有数值都会自动限制在合法范围内。

---

### 2️⃣ Time-Based System | 时间系统

- Records last interaction time  
- 长时间未互动会逐步降低 mood / trust  
- Frequent interaction raises mood / trust while consuming a little sleep  
- Sleeping for ~8 hours restores sleep to full  

The system reacts based on real-world time difference.  
系统会根据现实时间差做出变化。

---

### 3️⃣ Interactive Commands | 交互命令

Available commands:
pet
feed
play
scold
time
status
voice
quit

Users can modify the cat's state through these commands.  
用户可以通过命令改变猫的状态。

---

### 4️⃣ Persistent Storage | 状态持久化

State is saved in:
The cat’s status persists between program runs.  
关闭程序后状态不会重置。

---

### 5️⃣ Basic Random Event System | 基础随机事件系统

Random events may trigger after user interaction.  
每次用户输入后可能触发随机事件。

---

## 🚀 Planned Features (v0.3+) | 计划功能

- Emotion-dependent face system | 情绪关联表情系统
- Trust-based event probability | 信任值影响事件概率
- Dialogue system | 对话系统
- Personality traits | 性格系统
- Growth stages | 成长阶段
- Achievement system | 成就系统

---

## 🛠 Tech Stack | 技术栈

- Python 3
- JSON (State Persistence)
- Git (Version Control)

---

## 🎮 How to Run | 运行方式

Activate virtual environment:
source .venv/bin/activate

Run the program:
python -m catcompanion.main

---

## 🌱 Long-Term Vision | 长期愿景

To build an evolving, emotionally responsive digital companion system.  
构建一个会成长、会变化、具有情绪反馈的数字陪伴系统。

## 🧪 Reminder Testing | 定时提醒测试

1. 安装依赖（若尚未安装）：
   ```bash
   pip install schedule
   ```
2. 运行自动化测试：
   ```bash
   python -m unittest tests/test_reminder.py
   ```
3. 手动联调（真实播报）：
   - 运行主程序：`python main.py`
   - 将 `reminder.py` 里的提醒时间临时改成“当前时间 + 1 分钟”做快速验证。
   - 到点后应自动调用现有 TTS（`reactions.speak`）进行播报。
