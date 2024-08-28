package com.ericsson.springapi.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

@Document
@Getter
@Setter
@AllArgsConstructor
public class Product {
    @Id
    private String id;

    // data > applications > instances > date > metrics
    private HashMap<String, HashMap<String, HashMap<String, HashMap<String, String>>>> data;

    // Key Getters
    public Set<String> findApplications() {
        return data.keySet();
    }

    public Set<String> findInstancesInApplication(String application) {
        return data.get(application).keySet();
    }

    // Metrics Getters
    public Object findSpecificInstanceMetrics(String application, String instance, String date) {

        Map<String, Map<String, String>> metrics = new HashMap<>();

        if (data.containsKey(application) && data.get(application).containsKey(instance)
                && data.get(application).get(instance).containsKey(date)) {

            metrics.put(instance, data.get(application).get(instance).get(date));
        }

        return metrics.isEmpty()? null : metrics;
    }

    public Object findMetricsForEachInstanceInApplication(String application, String date) {

        Map<String, Map<String, String>> metrics = new HashMap<>();

        if (data.containsKey(application)) {
            for (String instance: data.get(application).keySet()) {
                metrics.put(instance, data.get(application).get(instance).get(date));
            }
        }

        return metrics.isEmpty()? null : metrics;
    }

    public Object findAllMetrics(String date) {

        Map<String, Map<String, String>> metrics = new HashMap<>();

        data.keySet().forEach(application -> {
            for (String instance : data.get(application).keySet()) {
                metrics.put(instance, data.get(application).get(instance).get(date));
            }
        });

        return metrics.isEmpty()? null : metrics;
    }

}
