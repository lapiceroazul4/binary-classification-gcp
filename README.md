<div style="display: flex; justify-content: center;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=00FFFF&size=25&center=true&vCenter=true&width=600&height=100&lines=SegFormer+Implementation;Computer+Vision;" alt="Typing SVG">
</div>


This project focuses on **image classification** using a **Convolutional Neural Network (CNN)**. It utilizes **Streamlit** for the interactive user interface, which allows users to upload images and receive real-time predictions of whether a person is wearing **Makeup** or not. The model is trained using a CNN architecture and is deployed using **Google Cloud Storage (GCS)** to serve the model checkpoint.

## Project Overview

In this project, we employ a Convolutional Neural Network (CNN) for the task of image classification *(You can check model.py)*. The goal is to classify images of people into two categories:
- **Makeup**
- **No Makeup**

## Technologies Used
- [**Streamlit**](https://streamlit.io/): For building the web application and user interface.
- [**PyTorch**](https://pytorch.org/): For training and deploying the CNN model.
- [**Google Cloud Storage**](https://cloud.google.com/storage): For storing the model checkpoint and accessing it for inference.
- [**PIL**](https://pypi.org/project/pillow/) and [**TorchVision**](https://pytorch.org/vision/): For image processing and transformation.

## How to use locally

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/lapiceroazul4/binary-classification-gcp.git
   cd binary-classification-gcp
   ```

> [!TIP]
> In the next step is highly recommended to use uv, since its way faster and the hole project was developed using uv. CHeck the docs [here](https://docs.astral.sh/uv/#uv)

2. Setup enviroment & requirements

    <details>
    <summary><b>Using <a href=https://docs.astral.sh/uv/>UV</a>></b></summary>

    - Install uv
        ```
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```
    - Create a uv project
        ```
        uv init
        ```
    - Install dependencies
        ```
        uv add -r requirements.txt
        ```
    - Run the app
        ```
        uv run streamlit run src/Homepage.py
        ```
    </details>

    <details>
    <summary><b>Using pip</b></summary>

    - Create the enviroment
        ```
        python -m venv .venv
        ```
    - Activate the enviroment
        ```
        source .venv/bin/activate # Linux
        ```
        ```
        .venv\Scripts\activate # Windows
        ```
    - Install dependencies
        ```
        pip install -r requirements.txt
        ```
    - Run the app
        ```
        streamlit run src/Homepage.py
        ```
    </details>

> [!NOTE]
> Keep in mind that the Dockerfile used to deploy its based on an image with uv preinstall.

## How to deploy

1. **Fork this repo**

     Forking a repository allows you to create a personal copy of someone else’s project. This is especially useful when you want to make changes to the project without affecting the original repository or just create your own instance.

    - In the top-right corner of the page, click the **"Fork"** button. This will create a copy of the repository under your own GitHub account.
    - Once the fork is complete, you will be redirected to the newly forked repository in your GitHub account.


2. **Setup Google Cloud Project and Billing**

    - First, go to [Create a Project](https://console.cloud.google.com/projectcreate?inv=1&invt=Abxo6A) make sure to be log in in the account you want to have the project

    - Provide all the info and click Create. If you get lost, you can [check this](https://developers.google.com/workspace/guides/create-project)

    - To setup the payment you'll need to add a Credit/Debit Card. Keep in mind that Google gives you 300$ in Credits, so, as long as you dont do something wrong there's nothing to worry about

3. **Setup Cloud Run**

    [Cloud Run](https://cloud.google.com/run) is serverless tool of GCP that allows you to create both functions and container-based servers. Cloud run handles the deployment, scaling, and traffic management, scaling your service from zero to hundreds of instances 
    
    - Once in cloud run click **connect repo** and connect your gcp account with your github account.

    - Then, you need to select the repo you fork in step 1, and click continue. 

    - Now go to the security tab and enable **Unauthenticated invocations**(This is importat so that your URL accesable from your web browser). [Docs](https://cloud.google.com/run/docs/authenticating/public?hl=en)

    - Once the deploy its done you can see the Cloud Run Service's URL. You can use this URL to access to your application

## If you got a problem

1. Ask ChatGPT
2. Google it 
3. Let me know at lapiceroazul@proton.me
