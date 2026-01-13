!git clone https://github.com/ggerganov/llama.cpp

!python llama.cpp/convert_hf_to_gguf.py \
    merged/merged_model \
    --outfile quantized/gguf/model-q4_0.gguf \
    --outtype q4_0

!python llama.cpp/convert_hf_to_gguf.py \
  merged/merged_model \
  --outfile quantized/gguf/model-f16.gguf \
  --outtype f16 \
  --verbose

%cd llama.cpp/

!cmake -B build -S . -DCMAKE_BUILD_TYPE=Release

!cmake --build build --config Release

./build/bin/llama-quantize \
  ../quantized/gguf/model-f16.gguf \
  ../quantized/gguf/model-q4_0.gguf \
  q4_0
