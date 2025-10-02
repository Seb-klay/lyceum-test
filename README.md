# lyceum-test
This is a test of the product of lyceum, a cloud computing company.

# Problems encountered
## 1. Computing between the CPU/GPU/automatic selection (using mnist.py)
While computing the mnist.py code (copied from the "get started page")
- (SUCCESS) using the CPU was working
- (FAILED) using the GPU crashed - nvlink_path: Couldn't find a suitable version of nvlink.
- (FAILED) using the automatic selection gave a http 500 with detail "All connection attempts failed" 

While computing the image-classification.py code
- (FAILED) using the automatic selection gave a http 500 with detail "All connection attempts failed"

While computing the nlp-project.ipynb (different results !)
- (FAILED) The Notebook was running cell after cell which allows to display results properly and is really good, i was not expecting that. However, i couldn't do a "pip install" which is the basic use of a notebook and the dependencies of the project.

## 2. Many broken links in the documentation/website
- menu bar of the main website
- doc : get started page
- doc : too many 404 redirect


# Questions
## 1. Name one feature that we should build next ?
You are currently developping the deployment of code on the servers. I tried some basic test that worked (but shouldn't check execution of AI-OLLAMA model because "monitoring execution/real-time output streaming" is still in development). Once this feature is done, an interesting thing (because it seems to be one of your main use case) would be to add a 2-click-deployment of models (eg. ollama and other available on dockerhub) for companies to quickly have bots in production for their business needs. The question of fine tuning is also to be asked but can be resolved.

## 2. What do you not like about the product ?
Having many broken links in the doc is a problem. It directly affects the use of the product and slows me down in my projects. Also, some basic problems encountered made it impossible for me to keep working on the project (eg. in my notebook).

## 3. Did anything not work as you'd expect ?
Several things. First of all, the automatic selection. I never could make it work. CPU and GPU where possible but only http 500 for the automatic selection. This is a pity because the feature is really interesting. Also, sometimes (depending on the code) i could compute code on CPU, sometimes on the GPU, but not always on both. This may be explained that the AI models require other code depeding on CPU or GPU. Last but not least, i was not able to do a pip install in my notebook (see point 1. above). 
