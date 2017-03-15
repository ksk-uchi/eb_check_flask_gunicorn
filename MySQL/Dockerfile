FROM mysql:5.7

EXPOSE 3306

ENV MYSQL_ROOT_USER root
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE test_schema
# 初期データをコンテナ起動時に実行
# ADD ./init.d/****.sql /docker-entrypoint-initdb.d/
