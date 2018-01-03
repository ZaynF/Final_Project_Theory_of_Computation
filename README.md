# Daily_Life_bot

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./state.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

1. **給予午餐、晚餐建議**
2. **播放音樂**

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"

### 吃飯
1. 先輸入"eating"來進入eating的state
2. 會進入"rice"、"noodle"、"fastfood"的選擇介面
3. 依上面給的三個選擇輸入對應的選擇就可以進入"rice"、"noodle"、"fastfood"的state
4. 之後bot會跑出對應的介面，接著user輸入"where"可在進入下一個state
5. bot會跑出其商店位置的資訊，之後便會回到"user"state
6. 指令懶人包:eating -> rice/noodle/fastfood -> where

### 音樂
1. 先輸入"music"來進入選擇介面
2. bot會給出"chinese"、"english"、"japanese"三個選擇
3. 輸入"chi"會到中文歌；輸入"eng"會到英文歌；輸入"jap"會到日文歌
4. 隨後各對應介面會給其曲目單，輸入對應的編號便可收到音樂檔案、或是網址
5. 給完之後，bot便會回到"user"state
6. 指令懶人包:music -> chi/eng/jap -> 1~7

## Author
[ZaynF](https://github.com/ZaynF)
