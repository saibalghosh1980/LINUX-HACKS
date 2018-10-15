with open('./src/main/resources/application.yml', 'r') as original:
    data = original.read()
    with open('./hawtio.txt', 'r') as hawtio:
        dataToWrite = hawtio.read()
        with open('./src/main/resources/application.yml', 'w') as modified:
            modified.write(dataToWrite + data)
