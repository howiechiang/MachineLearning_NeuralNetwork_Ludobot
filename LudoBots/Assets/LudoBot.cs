using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LudoBot : MonoBehaviour {

    public GameObject[] robotParts;
    public Color altColor = Color.red;

    // Use this for initialization
    void Start() {
        
        robotParts = new GameObject[8];             // Number of robot parts/objects
        
        //CreateBody(0, 0, 1, 0, 1, .2f, 1);
        CreateBody(0, 0, 2, 0, 5, 1, 5);
        CreateLeg(1, 1, 1, 0, .2f, 2, 0, 0, 0);
        CreateLeg(2, 0, 1, 1, .2f, 2, 0, 0, 0);
        CreateLeg(3, -1, 1, 0, .2f, 2, 0, 0, 0);
        CreateLeg(4, 0, 1, -1, .2f, 2, 0, 0, 0);
        //CreateLeg(5, 1, 1, 1, .2f, .5f, 0, 0, 0);
        //CreateLeg(6, 0, 1, 1, .2f, .5f, 0, 0, 0);
        //CreateLeg(7, -1, 1, 0, .2f, .5f, 0, 0, 0);
        //CreateLeg(8, 0, 1, -1, .2f, .5f, 0, 0, 0);

        
    }

    // Update is called once per frame
    void Update() {

    }

    // Create LudoBot Body
    void CreateBody(int index, float x, float y, float z, float length, float height, float width)
    {

        Vector3 position = new Vector3(x, y, z);
        Vector3 size = new Vector3(length, height, width);

        robotParts[index] = GameObject.CreatePrimitive(PrimitiveType.Cube);     //Include code here to make a cube, as it was done in the last assignment.
        robotParts[index].transform.position = position;                        //Code to place the robot body part in the desired location
        robotParts[index].transform.localScale = size;                          //set the local scale to match what was passed in.

        // Fill out a line to add a rigid body to the body part, so that it is physics enabled.
        robotParts[index].AddComponent<Rigidbody>();

        //additional code to color the part however you wish, or name the part something like "robot body" so that it can be better identified in the inspector, etc.
        //robotParts[index].GetComponent<Renderer>().material.color = Color.red;
        Debug.LogError(Color.red);
        //robotParts[index].GetComponent<Renderer>().material.color = Color.red;

        //robotParts[index].GetComponent<Renderer>().material.shader = Shader.Find("Specular");
        //robotParts[index].GetComponent<Renderer>().material.SetColor("_SpecColor", Color.red);

        //robotParts[index].GetComponent<Renderer>().material.color = Color.red;
        //Color color = gameObject.GetComponent<Renderer>().material.color;
        //gameObject.GetComponent<Renderer>().material.color = Color.red;

        //Debug.LogError("Completed body creation");
    }

    // Create LudoBot Leg
    void CreateLeg(int index, float x, float y, float z, float diameter, float height, float xRot, float yRot, float zRot)
    {

        Vector3 position = new Vector3(x, y, z);
        Vector3 size = new Vector3(diameter, height, diameter);
        Vector3 rotation = new Vector3(xRot, yRot, zRot);

        robotParts[index] = GameObject.CreatePrimitive(PrimitiveType.Cylinder); //Write code similar to what was done to create the cube, but now use a cylinder primitive rather than a cube primitive.
        robotParts[index].transform.position = position;
        robotParts[index].transform.localScale = size;
        robotParts[index].transform.eulerAngles = rotation;

        //add a rigid body 
        robotParts[index].AddComponent<Rigidbody>();

        //... //add additional code to set the body part's name, color, etc, if you wish to.
        //gameObject.GetComponent<Renderer>().material.color = Color.blue;
        //robotParts[index].GetComponent<Renderer>().material.color = Color.blue;
    }
}