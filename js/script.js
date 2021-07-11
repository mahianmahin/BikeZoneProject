let domNodes = {
    stickyNav: {
        first_banner: document.getElementById("first-banner"),
        sticky_nav: document.getElementById("sticky-nav"),
        nav_links: document.querySelector(".nav_links"),
        logo: document.getElementById("logo_img"),
        toggler: document.getElementById("toggler"),
        back_arrow: document.getElementById("back-btn"),
        sidemenu: document.getElementById("outer-main"),
        inner_main: document.getElementById("inner-main")
    },

    utilities: {
        scroll_btn: document.getElementById("sct")
    }
}

var smallScreen = false;

(() => {
    if (screen.width <= 1000) {
        smallScreen = true;
    } else {
        smallScreen = false;
    }
})();

window.addEventListener('resize', () => {
    location.reload();
});

// ====================== Navbar ======================= //

if (smallScreen) {
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
    
        if (scrolled >= 25) {
            domNodes.stickyNav.sticky_nav.style.background = "#fff";
            domNodes.stickyNav.sticky_nav.style.top = 0;
            domNodes.stickyNav.nav_links.classList.add("black");
            domNodes.stickyNav.logo.src = "./img/logos/logo-normal-small.png";
            domNodes.stickyNav.toggler.style.color = "black";
    
        } else {
    
            domNodes.stickyNav.sticky_nav.style.background = "rgba(0, 0, 0, 0.2)";
            domNodes.stickyNav.sticky_nav.style.top = 0;
            domNodes.stickyNav.nav_links.classList.remove("black");
            domNodes.stickyNav.logo.src = "./img/logos/logo-inverted-small.png";
            domNodes.stickyNav.toggler.style.color = "#fff";
        }
    
    });
} else {
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
    
        if (scrolled >= 25) {
            domNodes.stickyNav.sticky_nav.style.background = "#fff";
            domNodes.stickyNav.sticky_nav.style.top = 0;
            domNodes.stickyNav.nav_links.classList.add("black");
            domNodes.stickyNav.logo.src = "./img/logos/logo-normal-small.png";
    
        } else {
    
            domNodes.stickyNav.sticky_nav.style.background = "rgba(0, 0, 0, 0.2)";
            domNodes.stickyNav.sticky_nav.style.top = "57px";
            domNodes.stickyNav.nav_links.classList.remove("black");
            domNodes.stickyNav.logo.src = "./img/logos/logo-inverted-small.png";
        }
    
    });
}

// ====================== Navbar ======================= //

// ====================== Mobile navbar ======================= //

domNodes.stickyNav.back_arrow.addEventListener('click', () => {
    domNodes.stickyNav.sidemenu.style.width = 0;
    domNodes.stickyNav.inner_main.style.opacity = 0;
})

domNodes.stickyNav.toggler.addEventListener('click', () => {
    domNodes.stickyNav.sidemenu.style.width = "260px";
    setTimeout(() => {
        domNodes.stickyNav.inner_main.style.opacity = 1;
    }, 200);
});


// ====================== Mobile navbar ======================= //


// ==================== Scroll to top functionality =======================//

window.addEventListener('scroll', () => {
    let scrolled = window.scrollY;
    
    if (scrolled >= 1035) {
        domNodes.utilities.scroll_btn.style.right = "40px";
    } else {
        domNodes.utilities.scroll_btn.style.right = "-40px";
    }

    domNodes.utilities.scroll_btn.addEventListener('click', () => {
        document.documentElement.scrollTop = 0;
    });
});



// ==================== Scroll to top functionality =======================//


// ------------Featured bikes carousel section------------------//

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:false,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,

    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:3
        }
    }
})


// ------------Featured bikes carousel section------------------//