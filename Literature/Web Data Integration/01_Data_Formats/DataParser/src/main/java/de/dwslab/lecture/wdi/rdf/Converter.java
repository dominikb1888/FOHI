package de.dwslab.lecture.wdi.rdf;

import java.io.File;
import java.io.FileOutputStream;
import java.util.ArrayList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.DCTerms;
import org.apache.jena.vocabulary.RDFS;
import org.apache.jena.datatypes.xsd.XSDDatatype;



public class Converter {

	private static String NS_COUNTRY = "http://dwslab.de/wdi/country#";
	private static String NS_LANGUAGE = "http://dwslab.de/wdi/language#";
	private static Property POPULATION = ModelFactory.createDefaultModel()
			.createProperty("http://www.geonames.org/ontology#", "population");

	/**
	 * Converts the Mondial data set (XML) first into an JSON (for all countries
	 * in Europe) and creates than a RDF model from it which is stored.
	 * 
	 * @param args
	 *            -- not necessary
	 * @throws Exception
	 */
	public static void main(String[] args) throws Exception {

		// create the factory
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		// create a new document builder
		DocumentBuilder builder = factory.newDocumentBuilder();
		// parse a document
		Document doc = builder.parse("src/main/resources/mondial-3.0.xml");

		// define an xpath expression
		XPathFactory xpathFactory = XPathFactory.newInstance();
		XPath xpath = xpathFactory.newXPath();
		// select the countries of Europe and all their attributes
		XPathExpression expr = xpath
				.compile("/mondial/country[encompassed/@continent=/mondial/continent[@name='Europe']/@id]");
		NodeList list = (NodeList) expr.evaluate(doc, XPathConstants.NODESET);

		// create RDF
		Model model = ModelFactory.createDefaultModel();
		// create JSON
		Gson gson = new Gson();
		// iterate over all answers of the XPath
		for (int i = 0; i < list.getLength(); i++) {
			Node n = (Node) list.item(i);
			// get all attributes
			NamedNodeMap map = n.getAttributes();
			// store them in a json object
			JsonObject obj = new JsonObject();
			for (int j = 0; j < map.getLength(); j++) {
				obj.addProperty(map.item(j).getNodeName(), map.item(j)
						.getTextContent());
			}
			// select the languages
			ArrayList<String> languages = new ArrayList<String>();
			NodeList children = n.getChildNodes();
			for (int k = 0; k < children.getLength(); k++) {
				if (children.item(k).getNodeName().equals("languages")) {
					languages.add(children.item(k).getTextContent().trim());
				}
			}
			// add them to the json
			obj.add("languages", gson.toJsonTree(languages));
			// parse the json into a country object
			Country country = gson.fromJson(gson.toJson(obj), Country.class);
			// create a RDF resource from it
			createResource(country, model);
		}
		// store the resource data into a file
		FileOutputStream fos = new FileOutputStream(new File(
				"src/main/resources/mondial-3.0-europe-countries.rdf"));
		model.write(fos);
		// bw.close();
	}

	/**
	 * Creates the resource of a country adding the different properties.
	 * 
	 * @param The
	 *            country class as input
	 * @param model
	 *            The model
	 */
	private static void createResource(Country c, Model model) {
		Resource r = model.createResource(NS_COUNTRY + c.id);
		// add name
		r.addProperty(RDFS.label, c.name);
		// add language
		for (String lang : c.languages) {
			r.addProperty(
					DCTerms.language,
					model.createResource(NS_LANGUAGE + lang).addProperty(
							RDFS.label, lang));
		}
		// add population
		r.addProperty(POPULATION, c.population.toString(), XSDDatatype.XSDlong);

	}

}
