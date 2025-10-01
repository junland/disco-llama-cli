# CLI for Kubernetes Diagnostics

When used in a Kubernetes context, this CLI tool can assist with diagnosing issues such as connectivity problems. Although the tool is designed to work only with a local instance of Ollama, it can still be conceptually applied as if interacting with a Ollama instance(s) within a Kubernetes Cluster.

For example, if the Ollama instance wasn't exposed to the network or the Ollama instance was not running we could infer this based on the below command and output:

```bash
$> python .\main.py list
Error running model: Failed to connect to Ollama. Please check that Ollama is downloaded, running and accessible. https://ollama.com/download
```