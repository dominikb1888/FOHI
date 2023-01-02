package de.dwslab.lecture.wdi.json;

import com.google.gson.Gson;
import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class WDI_20200_RG2_Template6 {

    public static void main(String[] args) throws ParserConfigurationException,
            SAXException, IOException, XPathExpressionException {

        // create the factory

        // create a new document builder

        // parse a document


        // define an xpath expression


        // select the countries of Europe and all their attributes


        // create a gson object

        // open a writer to write some output


        // iterate over all country nodes

            // get the node

            // get the attributes of the node

            // create an empty hashmap

            // iterate over the attributes of the node

                // add the attribute name and the value to the map


            // parse the hashmap to a json string

            // write the string to the file

            // print the string to the console


        // close the writer


    }
}
