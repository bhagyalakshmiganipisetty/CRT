package qwerty.bhagi;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class controller {
    
    @GetMapping("/")
    public String index() {
       return "index";  // This corresponds to home.html in src/main/resources/templates
    }

    @GetMapping("/home")
    public String home() {
       return "home";  // This corresponds to home.html in src/main/resources/templates
    }

    @GetMapping("/login")
    public String login() {
        return "login";  // This corresponds to login.html in src/main/resources/templates
    }

    @GetMapping("/signup")
    public String signup() {
        return "signup";  // This corresponds to signup.html in src/main/resources/templates
    }

    @GetMapping("/about")
    public String about() {
        return "about";  // This corresponds to about.html in src/main/resources/templates
    }

    @GetMapping("/contact")
    public String contact() {
        return "contact";  // This corresponds to contact.html in src/main/resources/templates
    }

    @GetMapping("/nowshowing")
    public String nowShowing() {
        return "nowshowing";
    }
    
    @GetMapping("/comingsoon")
    public String comingSoon() {
        return "comingsoon";
    }
    
    @GetMapping("/bookings")
    public String bookings() {
        return "bookings";
    }
    
    @GetMapping("/reviews")
    public String reviews() {
        return "reviews";
    }
    
    @GetMapping("/pricing")
    public String pricing() {
        return "pricing";
    }
    
    @GetMapping("/faq")
    public String faq() {
        return "faq";
    }
}

