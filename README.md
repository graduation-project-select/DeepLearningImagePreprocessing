# deepLearningImagePreprocessing
딥러닝 이미지 전처리 코드

# 1. Data Augmentation
### dataAugmentation.py<br>
flip, rotation 가능

### dataAugmentation_tf.py<br>
https://www.notion.so/Augmentation-a28b225f02914c598b22f68ca0621e73#be56907987394937a2d10914460c9c7c 코드 활용<br>

# 2. Face Crop
### detectHuman.py<br>
./cvlib 라이브러리 필요<br>
사람 전체와 얼굴부위 감지 후 dataset에서 제거 또는 이미지 전처리<br>

1) 전신이 있는 경우 상의와 하의가 둘다 존재하기 때문에 dataset에서 제외 (haarcascade_fullbody.xml)<br>
-> 전신을 잘 감지하지 못해서 사용 X <br>
2) 얼굴을 감지한 경우 얼굴 rect의 밑변을 기준으로 위쪽을 제거(crop)<br>
-> 얼굴 제거 후 training시 loss 감소<br>

# 3. poseEstimation
참고: 
https://m.blog.naver.com/rhrkdfus/221531159811
