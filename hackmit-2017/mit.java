import java.io.PrintStream;
import java.time.Instant;
import java.time.temporal.ChronoUnit;

public class WarpCLI
{
  private static final long START_EPOCH = 2084704589L;

  public static void main(String[] paramArrayOfString)
  {
    Instant localInstant1 = Instant.now();
    Instant localInstant2 = Instant.ofEpochSecond(2084704589L);
    Instant localInstant3 = localInstant2.plus(1L, ChronoUnit.DAYS);
    if ((localInstant1.isAfter(localInstant2)) && (localInstant1.isBefore(localInstant3))) {
      System.out.println(new Object()
      {
        int t;

        public String toString()
        {
          byte[] arrayOfByte = new byte[47];this.t = 214297406;arrayOfByte[0] = ((byte)(this.t >>> 5));this.t = -857860058;arrayOfByte[1] = ((byte)(this.t >>> 17));this.t = -1631101334;arrayOfByte[2] = ((byte)(this.t >>> 12));this.t = 1301309819;arrayOfByte[3] = ((byte)(this.t >>> 15));this.t = 1395073438;arrayOfByte[4] = ((byte)(this.t >>> 2));this.t = -840406141;arrayOfByte[5] = ((byte)(this.t >>> 21));this.t = -1306721746;arrayOfByte[6] = ((byte)(this.t >>> 14));this.t = 1705118546;arrayOfByte[7] = ((byte)(this.t >>> 12));this.t = 735725342;arrayOfByte[8] = ((byte)(this.t >>> 14));this.t = 244174287;arrayOfByte[9] = ((byte)(this.t >>> 21));this.t = -1876121587;arrayOfByte[10] = ((byte)(this.t >>> 16));this.t = -2078845358;arrayOfByte[11] = ((byte)(this.t >>> 21));this.t = -801922987;arrayOfByte[12] = ((byte)(this.t >>> 11));this.t = -619565815;arrayOfByte[13] = ((byte)(this.t >>> 5));this.t = -860549072;arrayOfByte[14] = ((byte)(this.t >>> 21));this.t = -467691877;arrayOfByte[15] = ((byte)(this.t >>> 21));this.t = 1636835966;arrayOfByte[16] = ((byte)(this.t >>> 24));this.t = 1259589070;arrayOfByte[17] = ((byte)(this.t >>> 5));this.t = 483379908;arrayOfByte[18] = ((byte)(this.t >>> 22));this.t = 1996976621;arrayOfByte[19] = ((byte)(this.t >>> 24));this.t = -1398780041;arrayOfByte[20] = ((byte)(this.t >>> 21));this.t = 1737313860;arrayOfByte[21] = ((byte)(this.t >>> 5));this.t = -1576872829;arrayOfByte[22] = ((byte)(this.t >>> 2));this.t = 530794543;arrayOfByte[23] = ((byte)(this.t >>> 11));this.t = -590161434;arrayOfByte[24] = ((byte)(this.t >>> 22));this.t = 974256115;arrayOfByte[25] = ((byte)(this.t >>> 24));this.t = -1872862456;arrayOfByte[26] = ((byte)(this.t >>> 23));this.t = 851760043;arrayOfByte[27] = ((byte)(this.t >>> 6));this.t = -30729233;arrayOfByte[28] = ((byte)(this.t >>> 6));this.t = -176966777;arrayOfByte[29] = ((byte)(this.t >>> 11));this.t = -1545461594;arrayOfByte[30] = ((byte)(this.t >>> 8));this.t = 428223184;arrayOfByte[31] = ((byte)(this.t >>> 19));this.t = -1710927473;arrayOfByte[32] = ((byte)(this.t >>> 3));this.t = -1220611569;arrayOfByte[33] = ((byte)(this.t >>> 4));this.t = 1076533266;arrayOfByte[34] = ((byte)(this.t >>> 7));this.t = -1009975761;arrayOfByte[35] = ((byte)(this.t >>> 14));this.t = 1661013445;arrayOfByte[36] = ((byte)(this.t >>> 6));this.t = -1112807679;arrayOfByte[37] = ((byte)(this.t >>> 5));this.t = 62013580;arrayOfByte[38] = ((byte)(this.t >>> 9));this.t = -485532801;arrayOfByte[39] = ((byte)(this.t >>> 20));this.t = -595300941;arrayOfByte[40] = ((byte)(this.t >>> 9));this.t = -432365004;arrayOfByte[41] = ((byte)(this.t >>> 16));this.t = 521848667;arrayOfByte[42] = ((byte)(this.t >>> 15));this.t = -1924330278;arrayOfByte[43] = ((byte)(this.t >>> 14));this.t = -736096063;arrayOfByte[44] = ((byte)(this.t >>> 16));this.t = 422920356;arrayOfByte[45] = ((byte)(this.t >>> 10));this.t = -252798394;arrayOfByte[46] = ((byte)(this.t >>> 9));return new String(arrayOfByte);
        }
      }.toString());
    } else {
      System.out.println("It's not your time ;)");
      System.out.println(localInstant1);
      System.out.println(localInstant2);
      System.out.println(localInstant3);
    }
  }
}
