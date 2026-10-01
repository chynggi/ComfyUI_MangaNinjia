import huggingface_hub
import transformers.utils

# diffusers 0.27 (vendored code targets it) still imports names removed from huggingface_hub 1.x / transformers 5
if not hasattr(huggingface_hub, "cached_download"):
    huggingface_hub.cached_download = huggingface_hub.hf_hub_download
for _n, _v in (("FLAX_WEIGHTS_NAME", "flax_model.msgpack"), ("FLAX_WEIGHTS_INDEX_NAME", "flax_model.msgpack.index.json")):
    if not hasattr(transformers.utils, _n):
        setattr(transformers.utils, _n, _v)


from .MangaNinjia_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS,WEB_DIRECTORY

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"] 


