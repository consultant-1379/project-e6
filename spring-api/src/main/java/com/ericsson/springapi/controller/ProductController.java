package com.ericsson.springapi.controller;

import com.ericsson.springapi.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Set;

@RestController
@CrossOrigin
public class ProductController {


    private ProductService productService;

    //  Redid field injection to be constructor injection for testing purposes
    @Autowired
    public ProductController(ProductService productService) {
        this.productService = productService;
    }
    
    @GetMapping("/products/{id}/applications")
    public ResponseEntity <Set<String>> findApplicationsInProduct(@PathVariable String id) {
        return ResponseEntity.ok().body(productService.findApplicationsInProduct(id));
    }

    @GetMapping("/products/{id}/{application}/instances")
    public ResponseEntity <Set<String>> findInstancesOfApplicationInProduct(@PathVariable String id, @PathVariable String application) {
        return ResponseEntity.ok().body(productService.findInstancesOfApplicationInProduct(id, application));
    }

    @GetMapping("/products/{id}/{application}/{instance}/{date}")
    public ResponseEntity <Object> findSpecificInstanceMetricsInProduct(
            @PathVariable String id, @PathVariable String application, @PathVariable String instance,
            @PathVariable String date) {

        return ResponseEntity.ok().body(
                productService.findSpecificInstanceMetricsInProduct(id, application, instance, date)
        );
    }

    @GetMapping("/products/{id}/{application}/metrics/{date}")
    public ResponseEntity <Object> findMetricsForEachInstanceInApplicationInProduct(@PathVariable String id, @PathVariable String application, @PathVariable String date) {
        return ResponseEntity.ok().body(productService.findMetricsForEachInstanceInApplicationInProduct(id, application, date));
    }

    @GetMapping("/products/{id}/metrics/{date}")
    public ResponseEntity <Object> findAllMetricsInProductInProduct(@PathVariable String id, @PathVariable String date) {
        return ResponseEntity.ok().body(productService.findAllMetricsInProductInProduct(id, date));
    }

}
