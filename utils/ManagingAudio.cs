using System.Collections;
using System.Collections.Generic;
using UnityEditor.Experimental.GraphView;
using UnityEngine;

public class ManagingAudio : MonoBehaviour
{
    // Start is called before the first frame update
  
    public GameObject cube1;
    public GameObject cube2;
    public GameObject cube3;

    
    void Start()
    {
        //GetComponent<AudioSource>().Play();*
        cube1.GetComponent<AudioSource>().volume = 1;
        cube2.GetComponent<AudioSource>().volume = 0;
        cube3.GetComponent<AudioSource>().volume = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if ((cube1.activeSelf == false)&& (cube2.activeSelf == true) && (cube1.GetComponent<AudioSource>().volume>0))
        {
     
            cube1.GetComponent<AudioSource>().volume -= 0.001f;
            cube2.GetComponent<AudioSource>().volume += 0.001f;
           
            
        }
       

        else if ((cube2.activeSelf == false) && (cube2.GetComponent<AudioSource>().volume >0))
        {
            //GetComponent<AudioSource>().clip = audioclip_transition2;
            cube2.GetComponent<AudioSource>().volume -= 0.01f;
            cube3.GetComponent<AudioSource>().volume += 0.01f;

        }
    }
}
