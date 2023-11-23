# gittest

### git指令

#### 0.查看版本

```c
git -v
```



#### 1.初始化仓库

```markdown
git init
```



#### 2.克隆仓库

```c
git clone https://github.com/DeepDarkBoy48/clonetest.git
```

更换仓库名称

```c
git clone https://github.com/DeepDarkBoy48/clonetest.git 更换名称
```



#### 3.仓库配置

```c++
git config user.name 名字
```

```c
git config user.email 邮件
```

全局配置

```
git config --global user.name 名字
```

```
git config --global user.email 邮件
```



#### 4.文件操作

git状态

```
git status
```

将单个文件从工作区添加到暂存区

```
git add 文件名
```

将所有文件从工作区添加到暂存区

```
git add --all
```

将同一后缀的文件都添加到暂存区

```
git add *.后缀
```

将文件从暂存区移回工作区

```
git restore --staged 文件名
```

暂存区提交文件到仓库git

```
git commit -m 评论
```

查看提交的文件

```
git log
```

```
git log --oneline
```



#### 5.回退

##### 5.1误删文件后恢复（未提交）

```
git restore 需要恢复的文件
```

##### 5.2 误删文件后恢复（已提交）

```
git log --oneline
```

查看历史版本信息（示例）

```
36b01f3 (HEAD -> main) modifya
972825f newfileadd
4074514 (origin/main, origin/HEAD) Initial commit
```

```
git reset --hard 972825f
```

即回退到newfileadd那个旧版本，但是新版本也会消失

##### 5.3恢复旧版本的文件，但是保留新版本

```
36b01f3 (HEAD -> main) modifya
972825f newfileadd
4074514 (origin/main, origin/HEAD) Initial commit
```

```
git revert --hard 36b01f3
```



#### 6.分支操作

最少提价一个文件后才能创建分支

```
git branch 分支名称
```

查看分支

```
git branch -v
```

重命名分支

```
git branch -m 名称
```

切换分支

```
git checkout 分支名称
```

一步创建并切换分支

```
git checkout -b 分支名称
```

删除分支

```
git branch -d 分支名称
```

推送副分支 

```
git push --set-upstream origin user
```

分支合并
先切换到主分支使用merge合并

```
git merge 副分支
```



#### 7.tag

先查看历史版本

```
git log --oneline
```

```
93bb228 (HEAD -> main, origin/main, origin/HEAD) adduser
4567a5a combinetest
075a78a branchtestuser
dd7416c GitHub中是否看得见
36b01f3 modifya
972825f newfileadd
4074514 Initial commit
```

比如在第三个版本那里添加标签xuzitag

```
git tag xuzitag 075a78a
```

xuzitag是标签名称，075a78a是版本号

如下标签已经创建好了

```
93bb228 (HEAD -> main, origin/main, origin/HEAD) adduser
4567a5a combinetest
075a78a (tag: xuzitag, origin/user, user) branchtestuser
dd7416c GitHub中是否看得见
36b01f3 modifya
972825f newfileadd
4074514 Initial commit
```

此时想可以通过如下命令查看xuzitag后的版本信息

```
 git log --oneline xuzitag
```

删除标签

```
git tag -d xuzitag
```

通过标签创建分支

```
git checkout -b 分支名称 标签名称
```



#### 8.远程仓库推送

config文件中远程仓库的内容

```
[remote "origin"]
	url = https://github.com/DeepDarkBoy48/clonetest.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

远程推送

```
git push origin
```

这个命令将本地的 `main` 分支推送到远程仓库的 `origin` 上

```
git push -u origin main
```

远程拉取

```
git pull origin
```

```
git remote add origin (http)
```

查看添加的远程仓库

```
git remote -v
```



#### 9.ssh远程仓库链接（未研究）



#### 10.linux 

Linux系统下用gitlab部署自己的代码托管平台

虚拟机：VMware

### github官方手册

#### 1.create a new repository on the command line

```
echo "# test" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin https://github.com/DeepDarkBoy48/test.git
  git push -u origin main
```

#### 2.push an existing repository from the command line

```
git remote add origin https://github.com/DeepDarkBoy48/test.git
  git branch -M main
  git push -u origin main
```

#### 3.上传大文件

https://git-lfs.com/

检查安装

```
git lfs install
```

追踪要上传的大文件

```
git lfs track *
```

添加文件属性

```
git add .gitattributes
```

例如，要关联 .psd 文件，请输入以下命令：

```shell
$ git lfs track "*.文件后缀"
```

git push







