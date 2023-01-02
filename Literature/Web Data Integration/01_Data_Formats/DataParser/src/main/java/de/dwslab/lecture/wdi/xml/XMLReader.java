package de.dwslab.lecture.wdi.xml;

import java.io.IOException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.xml.sax.SAXException;

public class XMLReader {

	public static void main(String[] args) throws ParserConfigurationException,
			SAXException, IOException, XPathExpressionException {
		// create the factory
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		// create a new document builder
		DocumentBuilder builder = factory.newDocumentBuilder();
		// parse a document -- make sure the file is located on root level
		Document doc = builder.parse("src/main/resources/mondial-3.0.xml");

		// define an xpath expression
		XPathFactory xpathFactory = XPathFactory.newInstance();
		XPath xpath = xpathFactory.newXPath();
		// select the root node
		XPathExpression expr = xpath.compile("/*");
		// parse the node
		Node root = (Node) expr.evaluate(doc, XPathConstants.NODE);
		
	}

}
