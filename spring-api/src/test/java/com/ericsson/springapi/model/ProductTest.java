package com.ericsson.springapi.model;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.util.*;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

class ProductTest {

    @Mock
    private HashMap mockData;
    @Mock
    private HashMap mockApplications;
    @Mock
    private HashMap mockInstances;
    @Mock
    private HashMap mockMetrics;
    private Product product;

    @BeforeEach
    public void setUp() {
        mockData = mock(HashMap.class);
        mockApplications = mock(HashMap.class);
        mockInstances = mock(HashMap.class);
        mockMetrics = mock(HashMap.class);
        product = new Product("", mockData);
    }

    @Test
    void testFindApplications() {
        String item1 = "key1", item2 = "key2";
        //  Setup Sample return
        when(mockData.keySet()).thenReturn(
                new HashSet<>(Arrays.asList(item1, item2))
        );
        //  Call the method
        Set<String> applications = product.findApplications();
        //  Confirm the data
        assertTrue(applications.contains(item1));
        assertTrue(applications.contains(item2), "Checking if Product returns correct key-set.");
    }

    @Test
    void testFindInstancesInApplication() {
        String application = "test-app";
        String item1 = "key1", item2 = "key2";
        when(mockData.get(application)).thenReturn(mockApplications);
        when(mockApplications.keySet()).thenReturn(
                new HashSet<>(Arrays.asList(item1, item2))
        );
        Set<String> instances = product.findInstancesInApplication(application);
        assertTrue(instances.contains(item1));
        assertTrue(instances.contains(item2), "Checking if find Instance in application is called correctly.");
    }
}