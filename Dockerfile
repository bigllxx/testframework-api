FROM bigllxx/centos-allure:1.9.0
ADD . usr/testframwork
WORKDIR usr/testframwork
#RUN pip3 install -r requirements.txt
# java环境变量
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.272.b10-1.el7_9.x86_64
ENV JRE_HOME ${JAVA_HOME}/jre
ENV CLASSPATH .:${JAVA_HOME}/lib:${JRE_HOME}/lib
ENV PATH ${JAVA_HOME}/bin:$PATH

# EXPOSE 80
ENTRYPOINT python3 run.py
