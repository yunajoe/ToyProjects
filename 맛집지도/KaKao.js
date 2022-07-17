
function ClickFunction(){
    alert("010-8682-6840")

}

// 지도 생성
var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
var options = { //지도를 생성할 때 필요한 기본 옵션
	center: new kakao.maps.LatLng(37.5512, 126.9882), //지도의 중심좌표.
	level: 6//지도의 레벨(확대, 축소 정도)
};

var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴


// 지도 컨트롤러 

var mapTypeControl = new kakao.maps.MapTypeControl();

// 지도에 컨트롤을 추가해야 지도위에 표시됩니다
// kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
//map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);



// 마커를 표시할 위치와 title 객체 배열입니다 
const dataSet = [
    {
      title: "희락돈까스",
      address: "서울 영등포구 양산로 210",
      url: "https://www.youtube.com/watch?v=1YOJbOUR4vw&t=88s",
      category: "양식",
    },
    {
      title: "즉석우동짜장",
      address: "서울 영등포구 대방천로 260",
      url: "https://www.youtube.com/watch?v=1YOJbOUR4vw&t=88s",
      category: "한식",
    },
    {
      title: "아카사카",
      address: "서울 서초구 서초대로74길 23",
      url: "https://www.youtube.com/watch?v=5YeceyCzGx4",
      category: "일식",
    },
    {
        title: "IFC 스타벅스",
        address: " 서울 영등포구 국제금융로 10",
        url: "https://www.youtube.com/watch?v=9z9nkTPKVTw",
        category: "기타", 
    },
    {
        title: "애플하우스",
        address: "서울 서초구 신반포로 50",
        url: "https://www.youtube.com/watch?v=bXwXD1Gz0GM",
        category: "분식", 
    }, 
];


// var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
    
// 주소, 좌표 변환 객체 생성 

var geocoder = new kakao.maps.services.Geocoder();
function getCoordsByAddress(address) {
  // promise 형태로 반환
  return new Promise((resolve, reject) => {
    // 주소로 좌표를 검색합니다
    geocoder.addressSearch(address, function (result, status) {
      // 정상적으로 검색이 완료됐으면
      if (status === kakao.maps.services.Status.OK) {
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
        return resolve(coords);
      }
      reject(new Error("getCoordsByAddress Error: not valid Address"));
    });
  });
}

function getContent(data){
    // 유튜브 썸네일 id가져오기 
    let replaceUrl = data.url;
    let finUrl = '';
    replaceUrl = replaceUrl.replace("https://youtu.be/", '');
    replaceUrl = replaceUrl.replace("https://www.youtube.com/embed/", '');
    replaceUrl = replaceUrl.replace("https://www.youtube.com/watch?v=", '');
    finUrl = replaceUrl.split('&')[0];
    // windowinfo 사진 + 글 + 유튭링크
    return `
        <div class="infowindow">
            <div class="infowindow_img">
                <img src="https://img.youtube.com/vi/${finUrl}/mqdefault.jpg"  width="50" height="50"> 
            </div>
            <div class="infowindow_body">       
                <h5>${data.title}</h5>
                <p>${data.address}</p> 
                <a href=${data.url} target="_blank">유튜브영상보러가기</a>
            </div>
        </div> `; 
}


async function setMap() {
  for (var i = 0; i < dataSet.length; i++) {
    let position = await getCoordsByAddress(dataSet[i].address);

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
      map: map, // 마커를 표시할 지도
      position: position, // 마커를 표시할 위치
    });

    // 마커에 표시할 인포윈도우를 생성합니다
    var infowindow = new kakao.maps.InfoWindow({
        content: getContent(dataSet[i]), // 인포윈도우에 표시할 내용        
      });    

    // 클릭하면 windowinfo보이게 하기 
    kakao.maps.event.addListener(marker, 'click', makeOverListener(map, marker, infowindow));

    // addLister(marker라고 하면은 안 보인당)
    kakao.maps.event.addListener(map, 'mouseout', makeOutListener(infowindow));


    // 인포윈도우를 표시하는 클로저를 만드는 함수
    // 현재 인포윈도를 클릭하면은 클릭한 모든 장소의 윈포 윈도우가 뜬다.
    function makeOverListener(map, marker, infowindow) {
        return function() {
            infowindow.open(map, marker);
        };
    }

    // 인포윈도우를 닫는 클로저를 만드는 함수
    function makeOutListener(infowindow) {
        return function() {
            infowindow.close();
            };
        }     
  }
}
setMap();