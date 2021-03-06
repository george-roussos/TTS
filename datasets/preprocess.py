import os
import random
import librosa

def tts_cache(root_path, meta_file):
    """This format is set for the meta-file generated by extract_features.py"""
    txt_file = os.path.join(root_path, meta_file)
    items = []
    with open(txt_file, 'r', encoding='utf8') as f:
        for line in f:
            cols = line.split('| ')
            items.append(cols)  # text, wav_full_path, mel_name, linear_name, wav_len, mel_len
    random.shuffle(items)
    return items            


def tweb(root_path, meta_file):
    """Normalize TWEB dataset. 
    https://www.kaggle.com/bryanpark/the-world-english-bible-speech-dataset
    """
    txt_file = os.path.join(root_path, meta_file)
    items = []
    with open(txt_file, 'r') as ttf:
        for line in ttf:
            cols = line.split('\t')
            wav_file = os.path.join(root_path, cols[0]+'.wav')
            text = cols[1]
            items.append([text, wav_file])
    random.shuffle(items)
    return items
    

# def kusal(root_path, meta_file):
#     txt_file = os.path.join(root_path, meta_file)
#     texts = []
#     wavs = []
#     with open(txt_file, "r", encoding="utf8") as f:
#         frames = [
#             line.split('\t') for line in f
#             if line.split('\t')[0] in self.wav_files_dict.keys()
#         ]
#     # TODO: code the rest
#     return  {'text': texts, 'wavs': wavs}


def mailabs(root_path, meta_files):
        """Normalizes M-AI-Labs meta data files to TTS format"""
        folders = [os.path.dirname(f.strip()) for f in meta_files.split(",")]
        meta_files = [f.strip() for f in meta_files.split(",")]
        items = []
        for idx, meta_file in enumerate(meta_files):
                print(" | > {}".format(meta_file))
                folder = folders[idx]
                txt_file = os.path.join(root_path, meta_file)
                with open(txt_file, 'r') as ttf:
                        for line in ttf:
                                cols = line.split('|')
                                wav_file = os.path.join(root_path, folder, 'wavs', cols[0]+'.wav')
                                if os.path.isfile(wav_file):
                                        text = cols[1]
                                        items.append([text, wav_file])
                                else: 
                                        continue
        random.shuffle(items)
        return items


def ljspeech(root_path, meta_file):
    """Normalizes the LJSpeech meta data file to TTS format"""
    txt_file = os.path.join(root_path, meta_file)
    items = []
    with open(txt_file, 'r') as ttf:
        for line in ttf:
            cols = line.split('|')
            wav_file = os.path.join(root_path, 'wavs', cols[0]+'.wav')
            text = cols[1]
            items.append([text, wav_file])
    random.shuffle(items)
    return items

def ttsportuguese(root_path, meta_file):
    """Normalizes the TTS-Portuguese Corpus meta data file to TTS format"""
    txt_file = os.path.join(root_path, meta_file)
    items = []
    with open(txt_file, 'r') as ttf:
        for line in ttf:
            line = line.replace('==','|')
            cols = line.split('|')
            wav_file = os.path.join(root_path, cols[0])
            file_name = os.path.basename(wav_file).replace(".wav", "")
            if librosa.get_duration(filename=wav_file)< 0.6:
                print('ignored file:',file_name,'because is small')
                continue
            text = cols[1]
            items.append([text, wav_file])
    random.shuffle(items)
    return items

def nancy(root_path, meta_file):
    """Normalizes the Nancy meta data file to TTS format"""
    txt_file = os.path.join(root_path, meta_file)
    items = []
    with open(txt_file, 'r') as ttf:
        for line in ttf:
            id = line.split()[1]
            text = line[line.find('"')+1:line.rfind('"')-1]
            wav_file = root_path + 'wavn/' + id + '.wav'
            items.append([text, wav_file])
    random.shuffle(items)    
    return items
