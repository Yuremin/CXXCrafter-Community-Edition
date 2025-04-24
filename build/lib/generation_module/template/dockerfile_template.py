dockerfile_template = """
    ```Dockerfile
    FROM ubuntu:{ubuntu_version}

    ENV DEBIAN_FRONTEND=noninteractive

    RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://mirrors.aliyun.com/ubuntu/|g' /etc/apt/sources.list \
    && sed -i 's|http://security.ubuntu.com/ubuntu/|http://mirrors.aliyun.com/ubuntu/|g' /etc/apt/sources.list \
    && apt-get update \
    && apt-get upgrade -y

    # Install necessary packages
    Run apt-get update
    Run apt-get install -y build-essential
    Run apt-get install -y software-properties-common


    # Install Dependencies
    Run apt-get install -y {dependency1}
    Run apt-get install -y {dependency2}
    ...


    # Build the project with {build system}
    ....
    ```
    """


build_command_dict = {
    'cmake': """
        RUN mkdir build && \
        cd build && \
        cmake .. &&\
        make -j"$(nproc)"
    """
}