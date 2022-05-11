jQuery(function($){
    "use strict";

    var SLZ = window.SLZ || {};


    /*=======================================
     =             MAIN FUNCTION             =
     =======================================*/

    SLZ.mainFunction = function(){

        /*Google map*/
        var myLatLngHK = {lat: 22.277627, lng: 114.164995};
        var markerLatLngHK = {lat: 22.277627, lng: 114.164995};

        var myLatLngNY = {lat: 40.712780, lng: -74.006057};
        var markerLatLngNY = {lat: 40.712780, lng: -74.006057};

        var myLatLngSG = {lat: 1.356031, lng: 103.874896};
        var markerLatLngSG = {lat: 1.356031, lng: 103.874896};

        var customMapTypeId = 'map_style';

        // Create an array of styles.
        var styles = [
            {
                stylers: [
                    { hue: "#c8cccf" },
                    { saturation: -250 }
                ]
            },{
                featureType: "road",
                elementType: "geometry",
                stylers: [
                    { lightness: 100 },
                    { visibility: "simplified" }
                ]
            },{
                featureType: "road",
                elementType: "labels",
                stylers: [
                    { visibility: "off" }
                ]
            }
        ];

        // Create a new StyledMapType object, passing it the array of styles,
        // as well as the name to be displayed on the map type control.
        var styledMap = new google.maps.StyledMapType(styles,
            {name: "Alab Map"});

        var mapProp = {
            center: myLatLngNY,
            zoom:16,
            mapTypeId:google.maps.MapTypeId.ROADMAP,
            scrollwheel: false,
            draggable: false,
            disableDefaultUI: true,
            mapTypeControlOptions: {
                mapTypeIds: [google.maps.MapTypeId.ROADMAP, customMapTypeId]
            }
        };

        var flag = 0;
        function initialize() {

            if ($(window).width() <= 768) {
                mapProp.zoom = 9;
            }

            var map = new google.maps.Map(document.getElementById("map"),mapProp);
            map.mapTypes.set(customMapTypeId, styledMap);
            map.setMapTypeId(customMapTypeId);

            var image = {
                url: 'assets/img/icon/icon-location.png',
                // size: new google.maps.Size(71, 71),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(17, 34),
                scaledSize: new google.maps.Size(40, 40)
            };

            switch (flag) {
                case 0:
                    var marker = new google.maps.Marker({
                        position: markerLatLngNY,
                        map: map,
                        animation:google.maps.Animation.BOUNCE,
                        icon: image,
                        title: 'alab'
                    });
                    break;
                case 1:
                    var marker = new google.maps.Marker({
                        position: markerLatLngNY,
                        map: map,
                        animation:google.maps.Animation.BOUNCE,
                        icon: image,
                        title: 'alab'
                    });
                    break;
                case 2:
                    var marker = new google.maps.Marker({
                        position: markerLatLngHK,
                        map: map,
                        animation:google.maps.Animation.BOUNCE,
                        icon: image,
                        title: 'alab'
                    });
                    break;
                case 3:
                    var marker = new google.maps.Marker({
                        position: markerLatLngSG,
                        map: map,
                        animation:google.maps.Animation.BOUNCE,
                        icon: image,
                        title: 'alab'
                    });
                    break;

            }
        }
        google.maps.event.addDomListener(window, 'load', initialize);

        // Click Location
        $(".location-ny").on('click', function () {
            flag = 1;

            mapProp = {
                center: myLatLngNY,
                zoom:16,
                mapTypeId:google.maps.MapTypeId.ROADMAP,
                scrollwheel: false,
                disableDefaultUI: true,
                mapTypeControlOptions: {
                    mapTypeIds: [google.maps.MapTypeId.ROADMAP, customMapTypeId]
                }
            };

            initialize();

            google.maps.event.addDomListener(window, 'load', initialize);
        });

        $(".location-hk").on('click', function () {
            flag = 2;
            mapProp = {
                center: myLatLngHK,
                zoom:16,
                mapTypeId:google.maps.MapTypeId.ROADMAP,
                scrollwheel: false,
                disableDefaultUI: true,
                mapTypeControlOptions: {
                    mapTypeIds: [google.maps.MapTypeId.ROADMAP, customMapTypeId]
                }
            };
            initialize();
            google.maps.event.addDomListener(window, 'load', initialize);
        });

        $(".location-sg").on('click', function () {
            flag = 3;

            mapProp = {
                center: myLatLngSG,
                zoom:16,
                mapTypeId:google.maps.MapTypeId.ROADMAP,
                scrollwheel: false,
                disableDefaultUI: true,
                mapTypeControlOptions: {
                    mapTypeIds: [google.maps.MapTypeId.ROADMAP, customMapTypeId]
                }
            };

            initialize();

            google.maps.event.addDomListener(window, 'load', initialize);
        });

        $('.wrapper-map .over-map').on('click', function() {
            if ($(window).width() > 767) {
                $(".over-map").addClass("display-none");
                $(".branch").removeClass("display-none");
            } else {
                $(".over-map").removeClass("display-none");
                $(".branch").addClass("display-none");
            }
        });
        // Click branch
        $(".branch").on('click', function () {
            $(".over-map").removeClass("display-none");
            $(".branch").addClass("display-none");
        });
    };

    /*======================================
     =            INIT FUNCTIONS            =
     ======================================*/

    $(document).ready(function(){
        SLZ.mainFunction();
    });

    /*=====  End of INIT FUNCTIONS  ======*/
});