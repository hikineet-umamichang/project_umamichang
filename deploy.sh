#!/bin/bash

# エラーが発生した場合にスクリプトを停止する
set -e

# 1. リポジトリを最新の状態に更新
echo "Pulling latest changes from the repository..."
git pull

# 2. 仮想環境をアクティブにする
echo "Activating virtual environment..."
source venv/bin/activate

# 3. 必要な依存関係をインストールする
echo "Installing dependencies..."
pip install -r requirements.txt

# 4. Gunicorn サーバーを再起動する
echo "Restarting Gunicorn server..."
pkill gunicorn
gunicorn --bind 127.0.0.1:8000 -D run:app

# 5. Nginx を再起動する
echo "Restarting Nginx server..."
sudo systemctl restart nginx

# 6. デプロイが完了したことを通知
echo "Deployment completed successfully!"
