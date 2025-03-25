# Music Genres - Clustering

## 🔗 Kaynaklar
- Hugging Face Uygulaması: [Music Clustering Space](https://huggingface.co/spaces/btulftma/music-clustering)


## 📖 Giriş
Bu proje, müzik türlerini ses özelliklerine göre kümelemek için makine öğrenimi tekniklerini kullanmaktadır. Her bireyin müzik zevki farklıdır ve yaşam tarzı veya hobileriyle müzik tercihlerini tahmin etmek zordur. Müzik akış uygulamaları, kullanıcıların dinleme alışkanlıklarını analiz ederek benzer müzik önerileri sunabilir.

Bu projede, Spotify'dan alınan popüler şarkılar içeren bir veri seti ile çalışacağız. Veri setinde sanatçılar, şarkı isimleri ve her müziğin ses özellikleri yer almaktadır. Amacımız, bu özellikler temelinde müzik türlerini benzerliklerine göre gruplamaktır.

## 📊 Veri Sözlüğü
Bu veri kümesi, müzik parçalarının çeşitli özelliklerini içermektedir. Aşağıda her bir sütunun anlamı açıklanmaktadır:

| Sütun Adı | Açıklama |
|-----------|----------|
| Index     | Her bir müzik parçası için benzersiz bir tanımlayıcı. |
| Title     | Müzik parçasının başlığı. |
| Artist    | Müzik parçasını icra eden sanatçı veya grup. |
| Top Genre | Müzik parçasının en çok ait olduğu tür. |
| Year      | Müzik parçasının yayınlandığı yıl. |
| Beats Per Minute | Parçanın dakikada vuruş sayısını (BPM) belirtir. |
| Energy    | Parçanın enerji seviyesini (0-100 arası) gösterir. |
| Danceability | Parçanın dans edilebilirlik seviyesini (0-100 arası) belirtir. |
| Loudness  | Parçanın ses yüksekliğini (dB cinsinden) belirtir. |
| Liveness   | Parçanın canlı bir ortamda kaydedilip kaydedilmediğini gösterir. |
| Valence   | Parçanın duygusal içeriğini (0-100 arası) gösterir. |
| Length    | Müzik parçasının süresi (saniye cinsinden). |
| Acousticness | Parçanın akustik enstrümanlar içermesi olasılığını (0-100 arası) belirtir. |
| Speechiness | Parçanın konuşma içeriği (0-100 arası) belirtir. |
| Popularity | Parçanın popülaritesini belirtir. |

## 🔍 Veri Analizi
Veri seti üzerinde yapılan analizler sonucunda, müzik türleri arasındaki ilişkiler incelenmiştir. Özellikle, dans edilebilirlik, enerji, BPM gibi ses özelliklerinin kümeleme üzerinde önemli etkileri olduğu gözlemlenmiştir.

## 📈 Kümeleme
Kümeleme işlemi, K-Means algoritması kullanılarak gerçekleştirilmiştir. Optimum küme sayısını belirlemek için Elbow Method ve Silhouette Score analizi yapılmıştır. 

### Sonuçlar
Kümeleme sonucunda, 4 farklı müzik kümesi elde edilmiştir:
- **Küme 0**: Yüksek dans edilebilirlik ve BPM değerlerine sahip şarkılar içeriyor. Genellikle hareketli ve enerjik parçalar bu kümede yer alıyor.
- **Küme 1**: Daha akustik, düşük enerji seviyesine sahip şarkılar yoğunlukta. Bu kümedeki müzikler genellikle daha sakin ve dinlendirici.
- **Küme 2**: Popüler ve enerjik parçaların toplandığı bir küme. Bu küme, dinleyiciler tarafından sıkça tercih edilen hit şarkılardan oluşuyor.
- **Küme 3**: Daha düşük popülerliğe sahip, deneysel veya niş müzikler içeriyor. Bu küme, alternatif ve farklı müzik türlerine odaklanıyor.

## 📄 Sonuç
Kümeleme analizi, müzik türleri arasında belirli bir yapısal ayrım olduğunu göstermektedir. Elde edilen kümeler, kullanıcıların müzik tercihlerini daha iyi anlamak ve öneri sistemlerini geliştirmek için kullanılabilir. Böylece, kullanıcılar için daha kişiselleştirilmiş müzik önerileri sunulabilir.
