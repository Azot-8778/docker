#FROM ubuntu:22.04
#RUN apt update & apt install -y python3 && rm -rf /var/lib/apt/lists/*

#переменные окружения на этапе сборки
ARG py_ver=3.9

#скачиваем оптимальный образ
FROM python:${py_ver}-alpine

#переменные окружения запущенного контейнера
ENV TEST_ENV = ${py_ver}

#копируем файл с сортировкой
COPY . . 

#запускаем файл в образе
ENTRYPOINT [ "python3" ]
CMD [ "sort.py" ]
