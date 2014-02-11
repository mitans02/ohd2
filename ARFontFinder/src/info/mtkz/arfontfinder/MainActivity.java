package info.mtkz.arfontfinder;

import java.util.Vector;

import org.opencv.android.OpenCVLoader;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfPoint;
import org.opencv.core.Point;
import org.opencv.core.Scalar;

import es.ava.aruco.Board;
import es.ava.aruco.Marker;
import es.ava.aruco.android.Aruco3dActivity;

public class MainActivity extends Aruco3dActivity {
	static {
	    if (!OpenCVLoader.initDebug()) {
	        // Handle initialization error
	    }
	}
	
	@Override
	public void initDetectionParam() {
		mMarkerSize = 0.034f;	
	}

	final Scalar _bgcolor = new Scalar(255,0,0);
	final Scalar _fontcolor = new Scalar(0,0,0);
	
	@Override
	public void onDetection(Mat frame, Vector<Marker> detectedMarkers, int idSelected) {
		for(Marker m : detectedMarkers){
			Vector<Point> pts = m.getPoints();
			MatOfPoint mop = new MatOfPoint();
		    mop.fromList(pts);
		    Core.fillConvexPoly(frame, mop, _bgcolor);
		    
		    String cad = new String();
		    cad = "id="+m.getMarkerId();
		    // determine the centroid
		    Point cent = new Point(0,0);
		    for(int i=0;i<4;i++){
		    	cent.x += pts.get(i).x;
		    	cent.y += pts.get(i).y;
		    }
		    cent.x/=4.;
		    cent.y/=4.;
		    Core.putText(frame, cad, cent,Core.FONT_HERSHEY_SIMPLEX, 2.0,  _fontcolor ,2);
		}
	}

	@Override
	public void onBoardDetection(Mat mFrame, Board mBoardDetected, float probability) {
		
	}

}
